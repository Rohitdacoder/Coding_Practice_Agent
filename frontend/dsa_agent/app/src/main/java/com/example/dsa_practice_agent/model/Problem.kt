package com.example.dsa_practice_agent.model

data class Problem(
    val title: String = "",
    val difficulty: String = "",
    val platform: String = "",
    val link: String = "",
    val topic: String = "",
    val editorial: String = "",
    val summary: String = "",
    val tags: List<String> = emptyList(),
    val acceptance: Double = 0.0,
    val likes: Int = 0,
    val dislikes: Int = 0
)
