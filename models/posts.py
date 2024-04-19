import uuid

from sqlalchemy import Column, UUID, String, Text, ForeignKey

from config.database import Base


class Post(Base):
    __tablename__ = 'posts'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4(), index=True)
    title = Column(String, index=True)
    content = Column(Text, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))