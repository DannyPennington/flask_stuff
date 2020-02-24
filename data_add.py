from application import db
from application.models import Posts
post1 = Posts(first_name="Ben",  last_name="Hesketh", title="First Post", content="This is some data blah blah")
db.session.add(post1)
db.session.commit()
