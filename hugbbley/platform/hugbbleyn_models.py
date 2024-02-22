from sqlalchemy import (Column,
                        Integer,
                        String,
                        Text,
                        DateTime,
                        ForeignKey,
                        JSON)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class Entry(Base):
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), unique=True)
    batch_id = Column(String(36))
    type = Column(String(255))
    family_hash = Column(String(255), index=True)
    content = Column(Text)
    properties = Column(Text)
    tags = relationship("Tag", secondary="entry_tags")


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)


class EntryTag(Base):
    __tablename__ = 'entry_tags'

    entry_id = Column(Integer, ForeignKey('entries.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)


class Monitoring(Base):
    __tablename__ = 'monitoring'

    id = Column(Integer, primary_key=True)
    type = Column(String(255))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    duration = Column(Integer)
    request = Column(Text)
    response = Column(Text)


Base = declarative_base()


class Endpoint(Base):
    __tablename__ = 'endpoint'

    id = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False)
    http_method = Column(String(10), nullable=False)
    handler_function = Column(String(255), nullable=False)
    summary = Column(String(255))
    description = Column(Text)
    parameters = Column(JSON)
    response_model = Column(JSON)
    response_status_codes = Column(JSON)
    auth_required = Column(String(50))
    rate_limits = Column(String(255))
    tags = Column(String(255))
    deprecation_status = Column(String(50))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"<Endpoint(url='{self.url}', http_method='{self.http_method}')>"


class APICall(Base):
    __tablename__ = 'api_calls'

    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer, ForeignKey('endpoint_info.id'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    request_data = Column(Text)
    response_data = Column(Text)
    status_code = Column(Integer)

    # Define a relationship with EndpointInfo
    endpoint = relationship("EndpointInfo", back_populates="api_calls")

    def __repr__(self):
        return f"<APICall(endpoint_id='{self.endpoint_id}', timestamp='{self.timestamp}')>"
