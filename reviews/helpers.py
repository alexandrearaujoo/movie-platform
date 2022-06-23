def response_formatted(data):
    serializer_data = {
            **data,
            "critic": {
                "id": data["critic"]["id"],
                "first_name": data["critic"]["first_name"],
                "last_name": data["critic"]["last_name"]
            },
            "movie_id": data["movie"]["id"]
    }

    del serializer_data["movie"]

    return serializer_data