import requests
import pytest

url = "http://localhost:4200"

@pytest.fixture
def create_actor():
	new_actor = {
		"fullName": "actor",
		"birthday": "2024-11-11T10:59:49.118Z",
		"height": 180
	}
	response = requests.post(f"{url}/actor", json=new_actor)
	assert response.status_code == 201
	
	data = response.json()
	assert data["fullName"] == new_actor["fullName"]
	actor_id = data["id"]

	return actor_id

def test_create_actor():
	new_actor = {
		"fullName": "actor",
		"birthday": "2024-11-11T10:59:49.118Z",
		"height": 180
	}
	response = requests.post(f"{url}/actor", json=new_actor)
	assert response.status_code == 201
	
	data = response.json()
	assert data["fullName"] == new_actor["fullName"]

def test_get_actor(create_actor):
	actor_id = create_actor

	response = requests.get(f"{url}/actor/{actor_id}")
	assert response.status_code == 200

def test_get_actors():
	response = requests.get(f"{url}/actor")
	assert response.status_code == 200

	data = response.json()

	assert isinstance(data, list)
	assert len(data) > 0

def test_update_actor(create_actor):
	actor_id = create_actor
	
	updated_actor = {
		"fullName": "actor updated",
		"birthday": "2024-11-07T00:00:00.000Z",
		"height": 180
	}

	response = requests.patch(f"{url}/actor/{actor_id}", json=updated_actor)
	assert response.status_code == 200
	
	data = response.json()
	assert data["fullName"] == updated_actor["fullName"]

def test_delete_actor(create_actor):
	actor_id = create_actor

	response = requests.delete(f"{url}/actor/{actor_id}")
	assert response.status_code == 200