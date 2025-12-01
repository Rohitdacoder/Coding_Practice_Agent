package com.example.dsa_practice_agent.network

import android.content.Context
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import java.net.InetSocketAddress
import java.net.Socket

object ServerDiscovery {

    private const val PORT = 8000
    private const val TIMEOUT = 200

    suspend fun isServerAvailable(ip: String): Boolean {
        return withContext(Dispatchers.IO) {
            try {
                Socket().use { socket ->
                    socket.connect(InetSocketAddress(ip, PORT), TIMEOUT)
                    true
                }
            } catch (e: Exception) {
                false
            }
        }
    }

    suspend fun autoScanForServer(myIp: String): String? {
        val prefix = myIp.substringBeforeLast(".")  // 10.7.128.xxx

        for (i in 1..254) {
            val testIp = "$prefix.$i"
            if (isServerAvailable(testIp)) {
                return testIp
            }
        }
        return null
    }
}
