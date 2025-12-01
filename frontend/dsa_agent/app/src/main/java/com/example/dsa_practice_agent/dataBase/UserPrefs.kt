package com.example.dsa_practice_agent.dataBase

import android.content.Context
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

val Context.dataStore by preferencesDataStore("user_prefs")

object UserPrefs {

    private val KEY_USERNAME = stringPreferencesKey("leetcode_username")

    suspend fun saveUsername(context: Context, username: String) {
        context.dataStore.edit { prefs ->
            prefs[KEY_USERNAME] = username
        }
    }

    fun getUsername(context: Context): Flow<String?> {
        return context.dataStore.data.map { prefs ->
            prefs[KEY_USERNAME]
        }
    }
}
