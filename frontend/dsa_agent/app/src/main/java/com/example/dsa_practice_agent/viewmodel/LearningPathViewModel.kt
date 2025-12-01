package com.example.dsa_practice_agent.viewmodel

import android.content.Context
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.dsa_practice_agent.model.LearningPathItem
import com.example.dsa_practice_agent.repository.DSARepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.launch

class LearningPathViewModel : ViewModel() {
    private val repo = DSARepository()

    private val _path = MutableStateFlow<List<LearningPathItem>>(emptyList())
    val path = _path

    fun loadPath(context: Context) {
        viewModelScope.launch {
            val data = repo.getFullProfile(context, "https://leetcode.com/u/rohitdacoder/")
            _path.value = data.learning_path_preview
        }
    }
}
