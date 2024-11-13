import requests
import pytest

url = "http://localhost:4200"

@pytest.fixture
def create_genre():
	new_genre = {
		"name": "genre",
	}
	response = requests.post(f"{url}/genre", json=new_genre)
	assert response.status_code == 201
	
	data = response.json()
	assert data["name"] == new_genre["name"]
	genre_id = data["id"]

	return genre_id

def test_create_genre():
	new_genre = {
		"name": None,
	}
	response = requests.post(f"{url}/genre", json=new_genre)
	assert response.status_code == 400

def test_get_genre(create_genre):
	genre_id = create_genre

	response = requests.get(f"{url}/genre/{genre_id}")
	assert response.status_code == 200

def test_get_genres():
	response = requests.get(f"{url}/genre")
	assert response.status_code == 200

	data = response.json()

	assert isinstance(data, list)
	assert len(data) > 0

def test_update_genre(create_genre):
	genre_id = create_genre
	
	updated_genre = {
		"name": None,
	}

	response = requests.patch(f"{url}/genre/{genre_id}", json=updated_genre)
	assert response.status_code == 400

def test_delete_genre(create_genre):
	genre_id = create_genre

	response = requests.delete(f"{url}/genre/{genre_id}")
	assert response.status_code == 200
	
	response = requests.delete(f"{url}/genre/{genre_id}")
	assert response.status_code == 400