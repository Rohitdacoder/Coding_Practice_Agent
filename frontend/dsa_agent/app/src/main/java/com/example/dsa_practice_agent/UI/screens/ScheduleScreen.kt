package com.example.dsa_practice_agent.UI.screens

import android.net.Uri
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavHostController
import com.example.dsa_practice_agent.UI.components.ProblemCard
import com.example.dsa_practice_agent.model.Problem
import com.example.dsa_practice_agent.viewmodel.ScheduleViewModel
import com.google.gson.Gson

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ScheduleScreen(navController: NavHostController) {

    val vm: ScheduleViewModel = viewModel()
    val schedule by vm.schedule.collectAsState()
    val loading by vm.loading.collectAsState()

    val context = LocalContext.current

    LaunchedEffect(Unit) {
        vm.loadSchedule(
            context,
            "https://leetcode.com/u/rohitdacoder/"   // your profile
        )
    }


    Scaffold(
        topBar = { TopAppBar(title = { Text("7-Day Schedule") }) }
    ) { padding ->

        when {
            loading -> {
                CircularProgressIndicator(Modifier.padding(20.dp))
            }

            schedule.isEmpty() -> {
                Text("No schedule found", Modifier.padding(20.dp))
            }

            else -> {
                LazyColumn(Modifier.padding(padding)) {
                    schedule.forEach { (day, problems) ->

                        item {
                            Text(
                                day,
                                style = MaterialTheme.typography.titleMedium,
                                modifier = Modifier.padding(16.dp)
                            )
                        }

                        items(problems) { p ->
                            ProblemCard(
                                problem = p,
                                onClick = {
                                    val json = Uri.encode(Gson().toJson(p))
                                    navController.navigate("problem_detail/$json")
                                },
                                navController = navController
                            )
                        }
                    }
                }
            }
        }
    }
}
