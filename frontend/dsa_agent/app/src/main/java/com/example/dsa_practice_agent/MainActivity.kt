package com.example.dsa_practice_agent

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.ui.Modifier
import androidx.navigation.compose.rememberNavController
import com.example.dsa_practice_agent.UI.navigation.RootNavigationGraph
import com.example.dsa_practice_agent.UI.components.BottomNavBar
import com.example.dsa_practice_agent.ui.theme.DSATheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            DSATheme {
                val navController = rememberNavController()

                Scaffold(
                    bottomBar = { BottomNavBar(navController) }
                ) { innerPadding ->
                    // Wrap the navigation graph in a Box to apply the scaffold padding
                    Box(
                        modifier = Modifier.padding(innerPadding)
                    ) {
                        RootNavigationGraph(navController)
                    }
                }
            }
        }
    }
}
