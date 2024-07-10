# backend/app/routes/posts.py

from flask import Blueprint, request, jsonify
from ..models import db, Post
from ..middleware import token_required

posts = Blueprint('posts', __name__)

@posts.route('/', methods=['POST'])
@token_required
def create_post(current_user):
    data = request.get_json()
    new_post = Post(user_id=current_user.id, content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created successfully!"}), 201

@posts.route('/', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    result = []
    for post in posts:
        post_data = {
            'id': post.id,
            'user_id': post.user_id,
            'content': post.content,
            'created_at': post.created_at.strftime("%Y-%m-%d %H:%M:%S")  # Format the datetime
        }
        result.append(post_data)
    return jsonify(result)

@posts.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_post(current_user, id):
    post = Post.query.get_or_404(id)
    if post.user_id != current_user.id:
        return jsonify({"message": "Permission denied!"}), 403

    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted!"})
