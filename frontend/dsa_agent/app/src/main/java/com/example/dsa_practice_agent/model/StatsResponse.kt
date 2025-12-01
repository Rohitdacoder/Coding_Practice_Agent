package com.example.dsa_practice_agent.model

data class StatsResponse(
    val solved: Int,
    val topics: Map<String, Int>,
    val difficulty: DifficultyBreakdown
)

data class DifficultyBreakdown(
    val easy: Int,
    val medium: Int,
    val hard: Int
)
