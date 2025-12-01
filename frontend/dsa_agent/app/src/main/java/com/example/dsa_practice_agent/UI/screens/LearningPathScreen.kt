package com.example.dsa_practice_agent.UI.screens

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavHostController
import com.example.dsa_practice_agent.viewmodel.LearningPathViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LearningPathScreen(navController: NavHostController) {

    val vm: LearningPathViewModel = viewModel()
    val path by vm.path.collectAsState()
    val context = LocalContext.current

    LaunchedEffect(Unit) {
        vm.loadPath(context)
    }

    LazyColumn {
        items(path) { item ->
            Text("Day ${item.day} → ${item.topic}")
        }
    }
}