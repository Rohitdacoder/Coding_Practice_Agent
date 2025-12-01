package com.example.dsa_practice_agent.UI.screens

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Refresh
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavHostController
import com.example.dsa_practice_agent.UI.components.ProblemCard
import com.example.dsa_practice_agent.UI.components.ShimmerList
import com.example.dsa_practice_agent.model.Problem
import com.example.dsa_practice_agent.viewmodel.HomeViewModel
import com.valentinilk.shimmer.Shimmer
import android.net.Uri
import androidx.compose.ui.platform.LocalContext
import com.google.gson.Gson

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun HomeScreen(navController: NavHostController) {

    val context = LocalContext.current
    val vm: HomeViewModel = viewModel()
    val problems by vm.problems.collectAsState()
    val loading by vm.loading.collectAsState()

    LaunchedEffect(Unit) {
        vm.loadData(context)
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Today's Recommendations") },
                actions = {
                    IconButton(onClick = {
                        // Later: call API to refresh
                        vm.loadData(context)
                    }) {
                        Icon(Icons.Default.Refresh, contentDescription = "Refresh")
                    }
                }
            )
        }
    ) { padding ->

        Column(
            modifier = Modifier
                .padding(padding)
                .fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = androidx.compose.ui.Alignment.CenterHorizontally
        ) {
            when {
                loading -> {
                    ShimmerList()
                }

                problems.isEmpty() -> {
                    Text(
                        "No recommendations found",
                        modifier = Modifier.padding(16.dp)
                    )
                }

                else -> {

                    LazyColumn(
                        modifier = Modifier
                            .padding(horizontal = 12.dp)
                            .fillMaxSize()
                    ) {
                        items(problems) { problem ->
                            ProblemCard(
                                problem,
                                onClick = {
                                    val json = Uri.encode(Gson().toJson(problem))
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
