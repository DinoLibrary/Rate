package com.dino.smartrate

import android.os.Bundle
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.dino.rate.RatingDialog

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
        showDialogRate()
    }

    private fun showDialogRate() {
        val ratingDialog: RatingDialog = RatingDialog.Builder(this)
            .session(1)
            .date(1)
            .setNameApp(getString(R.string.app_name))
            .setIcon(R.mipmap.ic_launcher)
            .setEmail("vapp.helpcenter@gmail.com")
            .setDeviceInfo("1.0.1", "34", "Xiaomi")
            .isShowButtonLater(true)
            .isClickLaterDismiss(true)
            .setOnlickRate { rate ->
                Toast.makeText(this@MainActivity, "Rate$rate", Toast.LENGTH_SHORT).show()
            }
            .setTextButtonLater("Maybe Later")
            .setOnlickMaybeLate {
                Toast.makeText(this@MainActivity, "Feedback cannot be left blank", Toast.LENGTH_SHORT).show()
            }
            .ratingButtonColor(R.color.black)
            .build()

        ratingDialog.setCanceledOnTouchOutside(false)
        ratingDialog.show()
    }
}