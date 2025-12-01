package com.example.dsa_practice_agent.repository

import android.content.Context
import com.example.dsa_practice_agent.model.FullProfileResponse
import com.example.dsa_practice_agent.model.Problem
import com.example.dsa_practice_agent.network.ApiClient

class DSARepository {

    suspend fun getRecommendations(context: Context, profile: String): List<Problem> {
        return try {
            ApiClient.api(context).getRecommendations(profile)
        } catch (e: Exception) {
            e.printStackTrace()
            emptyList()
        }
    }

    suspend fun getSchedule(context: Context, profile: String): Map<String, List<Problem>> {
        return try {
            ApiClient.api(context).getSchedule(profile)
        } catch (e: Exception) {
            e.printStackTrace()
            emptyMap()
        }
    }

    suspend fun markSolved(context: Context, title: String): Boolean {
        return try {
            val response = ApiClient.api(context).markSolved(title)
            response["status"] == "ok"
        } catch (e: Exception) {
            e.printStackTrace()
            false
        }
    }

    suspend fun getFullProfile(context: Context, profile: String): FullProfileResponse {
        return ApiClient.api(context).getFullProfile(profile)
    }


}
