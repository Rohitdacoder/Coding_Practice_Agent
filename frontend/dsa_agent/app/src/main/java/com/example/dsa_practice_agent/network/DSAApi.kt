package com.example.dsa_practice_agent.network

import com.example.dsa_practice_agent.model.FullProfileResponse
import com.example.dsa_practice_agent.model.LearningPathItem
import com.example.dsa_practice_agent.model.Problem
import com.example.dsa_practice_agent.model.StatsResponse
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Query
import kotlinx.coroutines.Deferred
import retrofit2.Response

interface DSAApi {

    @GET("full_profile")
    suspend fun getFullProfile(
        @Query("profile") profile: String
    ): FullProfileResponse

    @GET("recommendations")
    suspend fun getRecommendations(
        @Query("profile") profile: String
    ): List<Problem>

    @GET("schedule")
    suspend fun getSchedule(
        @Query("profile") profile: String
    ): Map<String, List<Problem>>

    @POST("mark_solved")
    suspend fun markSolved(
        @Query("title") title: String
    ): Map<String, String>

    @GET("stats")
    suspend fun getStats(
        @Query("profile") profile: String
    ): StatsResponse

    @GET("path")
    suspend fun getLearningPath(@Query("profile") profile: String
    ): List<LearningPathItem>

}
