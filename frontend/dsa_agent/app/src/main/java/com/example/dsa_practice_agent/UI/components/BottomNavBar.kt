package com.example.dsa_practice_agent.UI.components

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.navigation.NavHostController

@Composable
fun BottomNavBar(navController: NavHostController) {

    NavigationBar {

        NavigationBarItem(
            selected = false,
            onClick = { navController.navigate("home") },
            icon = { Icon(Icons.Default.Home, contentDescription = null) },
            label = { Text("Home") }
        )

        NavigationBarItem(
            selected = false,
            onClick = { navController.navigate("schedule") },
            icon = { Icon(Icons.Default.Event, contentDescription = null) },
            label = { Text("Schedule") }
        )

        NavigationBarItem(
            selected = false,
            onClick = { navController.navigate("stats") },
            icon = { Icon(Icons.Default.BarChart, contentDescription = null) },
            label = { Text("Stats") }
        )

        NavigationBarItem(
            selected = false,
            onClick = { navController.navigate("learning_path") },
            icon = { Icon(Icons.Default.AutoGraph, contentDescription = null) },
            label = { Text("Path") }
        )
    }
}
