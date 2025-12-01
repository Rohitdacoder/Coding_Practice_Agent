package com.example.dsa_practice_agent.UI.screens

import androidx.compose.animation.core.*
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Star
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavHostController
import com.example.dsa_practice_agent.R
import com.example.dsa_practice_agent.dataBase.UserPrefs
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.first

@Composable
fun SplashScreen(navController: NavHostController) {

    val context = LocalContext.current
    val scale = remember { Animatable(0.8f) }

    LaunchedEffect(Unit) {
        scale.animateTo(1.2f, tween(700))
        scale.animateTo(1f, tween(400))
        delay(800)

        val saved = UserPrefs.getUsername(context).first()

        if (saved.isNullOrEmpty())
            navController.navigate("enter_id") { popUpTo("splash") { inclusive = true } }
        else
            navController.navigate("home") { popUpTo("splash") { inclusive = true } }
    }

    Box(
        Modifier.fillMaxSize(),
        contentAlignment = Alignment.Center
    ) {
        Column(horizontalAlignment = Alignment.CenterHorizontally) {

            // LeetCode Icon (You can add your own image)
            Icon(
                imageVector = Icons.Default.Star,
                contentDescription = "",
                tint = Color(0xFFFFA116),
                modifier = Modifier
                    .size(110.dp)
                    .scale(scale.value)
            )

            Spacer(Modifier.height(16.dp))

            Text(
                "DSA Practice Agent",
                style = MaterialTheme.typography.headlineMedium,
                color = Color.Black
            )
        }
    }
}

