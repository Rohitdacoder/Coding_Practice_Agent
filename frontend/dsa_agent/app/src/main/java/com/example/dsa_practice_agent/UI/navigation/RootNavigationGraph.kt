package com.example.dsa_practice_agent.UI.navigation

import android.net.Uri
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.NavType
import androidx.navigation.navArgument
import com.example.dsa_practice_agent.UI.screens.*
import com.example.dsa_practice_agent.model.Problem
import com.google.gson.Gson

@Composable
fun RootNavigationGraph(navController: NavHostController) {

    NavHost(
        navController = navController,
        startDestination = "splash"
    ) {

        composable("splash") { SplashScreen(navController) }
        composable("enter_id") { EnterIdScreen(navController) }

        composable("home") { HomeScreen(navController) }
        composable("schedule") { ScheduleScreen(navController) }
        composable("stats") { StatsScreen(navController) }
        composable("learning_path") { LearningPathScreen(navController) }

        composable(
            route = "problem_detail/{json}",
            arguments = listOf(navArgument("json") { type = NavType.StringType })
        ) { entry ->
            val json = entry.arguments?.getString("json") ?: ""
            val problem = Gson().fromJson(Uri.decode(json), Problem::class.java)
            ProblemDetailScreen(navController, problem)
        }
    }
}
