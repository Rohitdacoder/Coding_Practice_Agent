package com.example.dsa_practice_agent.viewmodel

import android.content.Context
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.dsa_practice_agent.dataBase.UserPrefs
import com.example.dsa_practice_agent.model.StatsResponse
import com.example.dsa_practice_agent.network.ApiClient
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.launch
import com.example.dsa_practice_agent.model.FullProfileResponse


class StatsViewModel : ViewModel() {

    private val _stats = MutableStateFlow<StatsResponse?>(null)
    val stats: StateFlow<StatsResponse?> = _stats

    private val _loading = MutableStateFlow(false)
    val loading: StateFlow<Boolean> = _loading

    fun loadStats(context: Context) {
        viewModelScope.launch {
            _loading.value = true

            val username = UserPrefs.getUsername(context).first() ?: ""
            val url = "https://leetcode.com/u/$username/"

            try {
                val api = ApiClient.api(context)
                val response = api.getStats(url)   // FullProfileResponse

                _stats.value = response // <-- THIS EXISTS
            } catch (e: Exception) {
                e.printStackTrace()
            }

            _loading.value = false
        }
    }
}
