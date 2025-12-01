package com.example.dsa_practice_agent.network

import android.content.Context

object ServerPrefs {

    private const val KEY_IP = "server_ip"

    fun saveIp(context: Context, ip: String) {
        context.getSharedPreferences("server_config", Context.MODE_PRIVATE)
            .edit()
            .putString(KEY_IP, ip)
            .apply()
    }

    fun getIp(context: Context): String? {
        return context.getSharedPreferences("server_config", Context.MODE_PRIVATE)
            .getString(KEY_IP, null)
    }
}
