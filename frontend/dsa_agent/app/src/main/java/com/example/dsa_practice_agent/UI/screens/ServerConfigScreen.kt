package com.example.dsa_practice_agent.UI.screens

import android.content.Context
import android.net.wifi.WifiManager
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.navigation.NavHostController
import com.example.dsa_practice_agent.network.ServerDiscovery
import com.example.dsa_practice_agent.network.ServerPrefs
import kotlinx.coroutines.launch

@Composable
fun ServerConfigScreen(navController: NavHostController) {

    val context = LocalContext.current
    val scope = rememberCoroutineScope()

    var ip by remember { mutableStateOf(ServerPrefs.getIp(context) ?: "") }
    var status by remember { mutableStateOf("") }
    var loading by remember { mutableStateOf(false) }

    fun getLocalIP(): String {
        val wifiManager = context.applicationContext.getSystemService(Context.WIFI_SERVICE) as WifiManager
        val ipInt = wifiManager.connectionInfo.ipAddress
        return ((ipInt and 0xff).toString() + "." +
                (ipInt shr 8 and 0xff) + "." +
                (ipInt shr 16 and 0xff) + "." +
                (ipInt shr 24 and 0xff))
    }

    Column(Modifier.padding(20.dp)) {

        Text("Server Configuration", style = MaterialTheme.typography.headlineSmall)
        Spacer(Modifier.height(20.dp))

        OutlinedTextField(
            value = ip,
            onValueChange = { ip = it },
            label = { Text("Server IP (Laptop)") },
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(Modifier.height(12.dp))

        Button(
            onClick = {
                scope.launch {
                    loading = true
                    status = "Checking..."

                    if (ServerDiscovery.isServerAvailable(ip)) {
                        ServerPrefs.saveIp(context, ip)
                        status = "Connected!"
                        navController.navigate("home")
                    } else {
                        status = "Server not reachable"
                    }
                    loading = false
                }
            },
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("Save & Connect")
        }

        Spacer(Modifier.height(12.dp))

        OutlinedButton(
            onClick = {
                scope.launch {
                    loading = true
                    status = "Scanning network..."

                    val localIp = getLocalIP()
                    val found = ServerDiscovery.autoScanForServer(localIp)

                    if (found != null) {
                        ip = found
                        ServerPrefs.saveIp(context, found)
                        status = "Found server at $found"
                        navController.navigate("home")
                    } else {
                        status = "No server found"
                    }

                    loading = false
                }
            },
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("Auto Discover Server")
        }

        Spacer(Modifier.height(12.dp))
        Text(status)
    }
}
