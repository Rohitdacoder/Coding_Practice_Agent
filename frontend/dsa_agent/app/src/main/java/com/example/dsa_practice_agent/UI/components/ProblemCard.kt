package com.example.dsa_practice_agent.UI.components

import android.net.Uri
import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.tween
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.unit.dp
import androidx.navigation.NavHostController
import com.example.dsa_practice_agent.model.Problem
import com.google.gson.Gson

@Composable
fun ProblemCard(problem: Problem, onClick: () -> Unit, navController: NavHostController) {

    // Fade + slide animation
    val enterAnim = remember { Animatable(0f) }

    LaunchedEffect(Unit) {
        enterAnim.animateTo(
            targetValue = 1f,
            animationSpec = tween(500)
        )
    }

    Card(
        modifier = Modifier
            .graphicsLayer(
                alpha = enterAnim.value,
                translationY = (1f - enterAnim.value) * 30
            )
            .fillMaxWidth()
            .padding(8.dp)
            .clickable { onClick() },  // Entire card clickable
        elevation = CardDefaults.cardElevation(4.dp)
    ) {

        Column(modifier = Modifier.padding(16.dp)) {

            /** TITLE */
            Text(
                text = problem.title,
                style = MaterialTheme.typography.titleLarge
            )

            Spacer(Modifier.height(8.dp))

            /** DIFFICULTY CHIP */
            AssistChip(
                onClick = {},
                label = { Text(problem.difficulty) },
                colors = AssistChipDefaults.assistChipColors(
                    containerColor = difficultyColor(problem.difficulty),
                    labelColor = Color.White
                )
            )

            Spacer(Modifier.height(6.dp))

            /** PLATFORM TEXT */
            Text(
                text = "Topic: ${problem.topic}",
                style = MaterialTheme.typography.bodySmall,
                color = Color.Gray
            )

            Spacer(Modifier.height(6.dp))

            Row {
                problem.tags.take(3).forEach { tag ->
                    AssistChip(
                        onClick = {},
                        label = { Text(tag) },
                        modifier = Modifier.padding(end = 4.dp)
                    )
                }
            }

            Spacer(Modifier.height(12.dp))

            /** VIEW DETAILS BUTTON */
            Button(onClick = {
                val json = Uri.encode(Gson().toJson(problem))
                navController.navigate("problem_detail/$json")
            }) {
                Text("View Details")
            }

        }
    }
}

/** Helper for difficulty colors */
@Composable
fun difficultyColor(diff: String): Color {
    return when (diff.lowercase()) {
        "easy" -> Color(0xFF4CAF50)
        "medium" -> Color(0xFFFFC107)
        "hard" -> Color(0xFFF44336)
        else -> Color.Gray
    }
}
