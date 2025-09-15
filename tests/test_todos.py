from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_create_todo():
    todo_data = {"title": "Test Todo", "description": "Test Description"}
    response = client.post("/api/v1/todos", json=todo_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == todo_data["title"]
    assert data["description"] == todo_data["description"]
    assert data["completed"] is False
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data

def test_get_todos():
    response = client.get("/api/v1/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_todo():
    # First create a todo
    todo_data = {"title": "Test Get Todo"}
    create_response = client.post("/api/v1/todos", json=todo_data)
    todo_id = create_response.json()["id"]
    
    # Then get it
    response = client.get(f"/api/v1/todos/{todo_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == todo_id
    assert data["title"] == todo_data["title"]

def test_update_todo():
    # First create a todo
    todo_data = {"title": "Test Update Todo"}
    create_response = client.post("/api/v1/todos", json=todo_data)
    todo_id = create_response.json()["id"]
    
    # Then update it
    update_data = {"title": "Updated Todo", "completed": True}
    response = client.put(f"/api/v1/todos/{todo_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == update_data["title"]
    assert data["completed"] == update_data["completed"]

def test_delete_todo():
    # First create a todo
    todo_data = {"title": "Test Delete Todo"}
    create_response = client.post("/api/v1/todos", json=todo_data)
    todo_id = create_response.json()["id"]
    
    # Then delete it
    response = client.delete(f"/api/v1/todos/{todo_id}")
    assert response.status_code == 204
    
    # Verify it's deleted
    get_response = client.get(f"/api/v1/todos/{todo_id}")
    assert get_response.status_code == 404