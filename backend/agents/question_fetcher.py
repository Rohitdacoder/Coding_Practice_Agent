import requests

def fetch_topic_questions(tag: str, limit=10):
    query = """
    query problemsetQuestions($tags: [String!], $limit: Int) {
      problemsetQuestions(filters: {tags: $tags}, limit: $limit) {
        title
        titleSlug
        difficulty
      }
    }
    """

    variables = {"tags": [tag], "limit": limit}

    resp = requests.post(
        "https://leetcode.com/graphql",
        json={"query": query, "variables": variables},
        timeout=10
    )

    data = resp.json()

    arr = data.get("data", {}).get("problemsetQuestions", [])

    return [
        {
            "title": p["title"],
            "difficulty": p["difficulty"],
            "link": f"https://leetcode.com/problems/{p['titleSlug']}/"
        }
        for p in arr
    ]
