from http_utils import *

# URL of API
API_URL = "https://ygwt22lk24.execute-api.us-east-1.amazonaws.com/prod"

bucket_name = "hw06-harsh"

def test_list_buckets():
    response_body = get(f"{API_URL}/list")
    assert isinstance(response_body, list), "Response body is not a list."
    expected_buckets = ['hw04-harsh', 'hw05-harsh', 'hw06-harsh']
    for bucket in expected_buckets:
        assert bucket in response_body, f"Bucket {bucket} not found in response."

    print("Test passed: List of buckets retrieved successfully.")

def test_list_objects_in_bucket():
    list_objects_url = f"{API_URL}/{bucket_name}"
    response = get(list_objects_url)
    assert isinstance(response, list), "Response is not a list."
    assert len(response) > 0, "No objects found in the bucket."
    expected_object_key = "example.txt"  # Example of an existing object in bucket
    assert expected_object_key in response, f"Expected object key '{expected_object_key}' not found in the list."
    print(f"Test passed: List of objects in bucket '{bucket_name}' retrieved successfully.")

def test_upload_file():
    object_name = "demo123.txt" 
    file_content_base64 = read_file_into_base64_string('./hw06/demo123.txt')

    post_data = create_post_data_for_post_object(bucket_name, object_name, file_content_base64)

    post_response = post(f"{API_URL}/{bucket_name}", post_data)

    assert hasattr(post_response, 'status_code'), "Response does not have a status_code attribute."
    assert post_response.status_code == 200, f"Expected status code 200, got {post_response.status_code}"

    response_body = post_response.json()
    assert "successfully uploaded" in response_body.get('message', ''), "File upload message not found in the response."

    print("Test passed: File uploaded successfully.")

def test_delete_object_from_bucket():
    object_name = "example2.txt"  # The name of the object you want to delete

    delete_url = f"{API_URL}/{bucket_name}/{object_name}"
    
    delete_response = delete(delete_url)

    assert hasattr(delete_response, 'status_code'), "Response does not have a status_code attribute."
    assert delete_response.status_code == 200, f"Unexpected HTTP status code: {delete_response.status_code}"

    response_body = delete_response.json()
    assert "successfully deleted" in response_body.get('message', ''), "Object deletion message not found in the response."

    print(f"Test passed: Object '{object_name}' successfully deleted from bucket '{bucket_name}'.")
