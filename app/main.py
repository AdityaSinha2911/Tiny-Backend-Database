from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from . import models, database, schema
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

# Add session middleware for admin authentication
app.add_middleware(SessionMiddleware, secret_key="your-secret-key-change-this")

models.Base.metadata.create_all(bind=database.engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Serve Form Page
@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# Submit Form
@app.post("/submit")
def submit_application(app_data: schema.ApplicationCreate, db: Session = Depends(get_db)):
    
    new_app = models.Application(
        name=app_data.name,
        email=app_data.email,
        phone=app_data.phone,
        course=app_data.course
    )
    
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    
    return {"message": "Application submitted successfully"}

# Admin Login Page
@app.get("/admin-login", response_class=HTMLResponse)
def admin_login_page(request: Request):
    return templates.TemplateResponse("admin_login.html", {"request": request})

# Admin Login Handler
@app.post("/admin-login", response_class=HTMLResponse)
async def admin_login(request: Request):
    form_data = await request.form()
    password = form_data.get("password")
    
    # Admin password (change this to something secure)
    ADMIN_PASSWORD = "Admin@123"
    
    if password == ADMIN_PASSWORD:
        request.session["admin_authenticated"] = True
        return RedirectResponse(url="/admin-dashboard", status_code=302)
    else:
        return templates.TemplateResponse("admin_login.html", {"request": request, "error": "Invalid password"})

# Admin Dashboard (Protected)
@app.get("/admin-dashboard", response_class=HTMLResponse)
def admin_dashboard(request: Request, db: Session = Depends(get_db)):
    # Check if user is authenticated
    if "admin_authenticated" not in request.session:
        return RedirectResponse(url="/admin-login", status_code=302)
    
    applications = db.query(models.Application).all()
    return templates.TemplateResponse("admin_dashboard.html", {
        "request": request,
        "applications": applications,
        "total_applications": len(applications)
    })

# Logout
@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=302)

# Delete Application (Admin)
@app.delete("/admin/delete/{app_id}")
def delete_application(app_id: int, request: Request, db: Session = Depends(get_db)):
    # Check if user is authenticated
    if "admin_authenticated" not in request.session:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    app_to_delete = db.query(models.Application).filter(models.Application.id == app_id).first()
    if not app_to_delete:
        raise HTTPException(status_code=404, detail="Application not found")
    
    db.delete(app_to_delete)
    db.commit()
    
    return {"message": "Application deleted successfully"}

# Admin Route
@app.get("/admin")
def view_applications(db: Session = Depends(get_db)):
    applications = db.query(models.Application).all()
    return applications