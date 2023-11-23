from httpx import AsyncClient


async def test_register(async_client: AsyncClient):
    req = await async_client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "password": "string",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
            "username": "test",
        },
    )
    assert req.status_code == 201


async def test_login(async_client: AsyncClient):
    req = await async_client.post(
        "/auth/login",
        data={
            "username": "test@example.com",
            "password": "string",
        },
    )
    assert req.status_code == 204
