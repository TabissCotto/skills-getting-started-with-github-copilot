def test_unregister_participant_removes_their_email_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    unregister_response = client.delete(f"/activities/{activity_name}/signup?email={email}")
    assert unregister_response.status_code == 200

    # Assert
    response = client.get("/activities")
    assert response.status_code == 200
    assert email not in response.json()[activity_name]["participants"]
