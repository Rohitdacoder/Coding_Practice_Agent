import requests

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"

def fetch_leetcode_stats(username):
    """
    Fetch real stats from LeetCode GraphQL API.
    Username example: "rohitdacoder"
    Returns dict with solved counts + topic stats.
    """

    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/{username}/",
        "User-Agent": "Mozilla/5.0"
    }

    query = {
        "query": """
        query userProfile($username: String!) {
          matchedUser(username: $username) {
            username
            submitStatsGlobal {
              acSubmissionNum {
                difficulty
                count
              }
            }
            tagProblemCounts{
              advanced {
                tagName
                problemsSolved
              }
              intermediate {
                tagName
                problemsSolved
              }
              fundamental {
                tagName
                problemsSolved
              }
            }
          }
        }
        """,
        "variables": {"username": username}
    }

    response = requests.post(LEETCODE_GRAPHQL_URL, json=query, headers=headers)

    if response.status_code != 200:
        print("Error fetching LeetCode data.")
        return None

    data = response.json().get("data", {}).get("matchedUser", None)
    if data is None:
        return None

    # Difficulty Stats
    diff_stats = data["submitStatsGlobal"]["acSubmissionNum"]
    difficulty = {
        item["difficulty"].lower(): item["count"]
        for item in diff_stats
    }

    # Topic Stats
    topic_stats = {}
    tag_sections = ["advanced", "intermediate", "fundamental"]
    for section in tag_sections:
        for item in data["tagProblemCounts"][section]:
            topic = item["tagName"]
            solved = item["problemsSolved"]
            topic_stats[topic] = topic_stats.get(topic, 0) + solved

    # Final Dict
    return {
        "solved": sum(difficulty.values()),
        "difficulty": difficulty,
        "topics": topic_stats
    }
