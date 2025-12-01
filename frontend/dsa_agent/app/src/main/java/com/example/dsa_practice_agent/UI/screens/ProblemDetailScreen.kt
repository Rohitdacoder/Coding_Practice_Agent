package com.example.dsa_practice_agent.UI.screens

import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavHostController
import com.example.dsa_practice_agent.model.Problem
import com.example.dsa_practice_agent.viewmodel.HomeViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ProblemDetailScreen(navController: NavHostController,problem: Problem) {

    val context = LocalContext.current
    val vm: HomeViewModel = viewModel()


    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(problem.title) },
                navigationIcon = {
                    IconButton(onClick = { navController.popBackStack() }) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Back")
                    }
                }
            )
        }
    ) { padding ->

        Column(
            modifier = Modifier
                .padding(padding)
                .padding(16.dp)
        ) {

            //Text("Title: ${problem.title}")
            Text("Difficulty: ${problem.difficulty}", style = MaterialTheme.typography.titleMedium)
            Text("Topic: ${problem.topic}")
            Text("Platform: ${problem.platform}")

            Spacer(Modifier.height(12.dp))

            Row {
                problem.tags.forEach { tag ->
                    AssistChip(
                        label = { Text(tag) },
                        onClick = {},
                        modifier = Modifier.padding(end = 6.dp)
                    )
                }
            }

            Spacer(Modifier.height(20.dp))

            Text("Summary:", style = MaterialTheme.typography.titleLarge)
            Text(problem.summary)

            Spacer(Modifier.height(20.dp))

            Text("Editorial:", style = MaterialTheme.typography.titleMedium)
            Text(problem.editorial)

            Spacer(Modifier.height(30.dp))

            Button(
                onClick = {
                    val intent = Intent(Intent.ACTION_VIEW, Uri.parse(problem.link))
                    context.startActivity(intent)
                },
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("Open Problem")
            }

            Spacer(Modifier.height(10.dp))

            OutlinedButton(
                onClick = {
                    vm.markSolved(context,problem)  // ⬅ call ViewModel
                    navController.popBackStack()
                },
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("Mark as Solved")
            }
        }
    }
}
