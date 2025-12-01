package com.example.dsa_practice_agent.viewmodel

import android.content.Context
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.dsa_practice_agent.model.Problem
import com.example.dsa_practice_agent.repository.DSARepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class ScheduleViewModel : ViewModel() {

    private val repo = DSARepository()

    private val _schedule = MutableStateFlow<Map<String, List<Problem>>>(emptyMap())
    val schedule: StateFlow<Map<String, List<Problem>>> = _schedule

    private val _loading = MutableStateFlow(true)
    val loading: StateFlow<Boolean> = _loading

    fun loadSchedule(context: Context, profile: String) {
        viewModelScope.launch {
            _loading.value = true
            val result = repo.getSchedule(context, profile)
            _schedule.value = result
            _loading.value = false
        }
    }

    init {
        // auto load on screen open
        // Replace with your real profile
        // Example:
        // loadSchedule(context, "https://leetcode.com/u/rohitdacoder/")
    }
}
