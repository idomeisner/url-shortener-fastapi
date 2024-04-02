from pydantic import BaseModel


class URLBase(BaseModel):
    target_url: str


class URL(URLBase):
    is_active: bool
    clicks: int

    class Config:
        # work with a database model
        orm_mode = True


class URLInfo(URL):
    url: str
    admin_url: str
