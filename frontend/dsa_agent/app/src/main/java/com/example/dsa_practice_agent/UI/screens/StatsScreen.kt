package com.example.dsa_practice_agent.UI.screens

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavHostController
import com.example.dsa_practice_agent.viewmodel.StatsViewModel
import me.bytebeats.views.charts.bar.BarChart
import me.bytebeats.views.charts.bar.BarChartData
import me.bytebeats.views.charts.pie.PieChart
import me.bytebeats.views.charts.pie.PieChartData

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun StatsScreen(navController: NavHostController) {

    val context = LocalContext.current
    val vm: StatsViewModel = viewModel()

    val stats by vm.stats.collectAsState()
    val loading by vm.loading.collectAsState()

    LaunchedEffect(Unit) {
        vm.loadStats(context)
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Your Stats") },
                navigationIcon = {
                    IconButton(onClick = { navController.popBackStack() }) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Back")
                    }
                }
            )
        }
    ) { padding ->

        if (loading || stats == null) {
            Box(
                modifier = Modifier.fillMaxSize().padding(padding),
                contentAlignment = Alignment.Center
            ) {
                CircularProgressIndicator()
            }
            return@Scaffold
        }

        val totalSolved = stats!!.solved
        val easy = stats!!.difficulty.easy
        val medium = stats!!.difficulty.medium
        val hard = stats!!.difficulty.hard
        val topics = stats!!.topics

        LazyColumn(
            modifier = Modifier.padding(padding).fillMaxSize().padding(16.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {

            item {
                Text("Total Solved: $totalSolved", style = MaterialTheme.typography.headlineMedium)
                Spacer(Modifier.height(20.dp))
            }

            item {
                Text("Difficulty Breakdown", style = MaterialTheme.typography.titleMedium)
                Spacer(Modifier.height(10.dp))

                PieChart(
                    pieChartData = PieChartData(
                        slices = listOf(
                            PieChartData.Slice(easy.toFloat(), Color(0xFF4CAF50)),
                            PieChartData.Slice(medium.toFloat(), Color(0xFFFFC107)),
                            PieChartData.Slice(hard.toFloat(), Color(0xFFF44336))
                        )
                    ),
                    modifier = Modifier.height(250.dp).fillMaxWidth(0.9f)
                )
                Spacer(Modifier.height(20.dp))
            }

            item {
                Text("Topics Performance", style = MaterialTheme.typography.titleMedium)
                Spacer(Modifier.height(10.dp))

                BarChart(
                    barChartData = BarChartData(
                        bars = topics.map { (name, count) ->
                            BarChartData.Bar(
                                value = count.toFloat(),
                                label = name,
                                color = Color(0xFF2196F3)
                            )
                        }
                    ),
                    modifier = Modifier.fillMaxWidth().height(240.dp)
                )
                Spacer(Modifier.height(30.dp))
            }

            item {
                Text("Topic Breakdown:", style = MaterialTheme.typography.titleMedium)
                Spacer(Modifier.height(10.dp))

                topics.forEach { (name, count) ->
                    Text("• $name — $count")
                }

                Spacer(Modifier.height(40.dp))
            }
        }
    }
}
