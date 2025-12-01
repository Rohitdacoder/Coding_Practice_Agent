package com.example.dsa_practice_agent.model

data class FullProfileResponse(
    val user_stats: StatsResponse,
    val weak_topics: List<String>,
    val recommendations: List<Problem>,
    val schedule: Map<String, List<Problem>>,
    val learning_path_preview: List<LearningPathItem>,
    val recent: List<Problem>
)
