import pytest
from core.fixtures.user import user
from core.post.models import Post

@pytest.mark.django_db
def test_create_user(user):
    post = Post.objects.create(author=user, body="Test body Post")
    assert post.author == user
    assert post.body == "Test body Post"