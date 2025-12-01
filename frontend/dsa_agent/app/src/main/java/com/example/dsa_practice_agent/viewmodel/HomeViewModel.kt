package com.example.dsa_practice_agent.viewmodel

import android.content.Context
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.dsa_practice_agent.model.Problem
import com.example.dsa_practice_agent.repository.DSARepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class HomeViewModel : ViewModel() {

    private val repo = DSARepository()

    private val _problems = MutableStateFlow<List<Problem>>(emptyList())
    val problems: StateFlow<List<Problem>> = _problems

    private val _loading = MutableStateFlow(true)
    val loading: StateFlow<Boolean> = _loading

    fun loadData(context: Context) {
        viewModelScope.launch {
            _loading.value = true
            _problems.value = repo.getRecommendations(
                context,
                "https://leetcode.com/u/rohitdacoder/"
            )
            _loading.value = false
        }
    }

    fun markSolved(context: Context,problem: Problem) {
        viewModelScope.launch {
            val ok = repo.markSolved(context,problem.title)

            if (ok) {
                // remove from current list
                _problems.value = _problems.value.filter { it.title != problem.title }
            }
        }
    }
}
