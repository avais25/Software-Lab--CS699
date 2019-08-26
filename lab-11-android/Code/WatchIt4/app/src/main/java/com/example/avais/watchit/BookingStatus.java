package com.example.avais.watchit;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.TextView;

public class BookingStatus extends AppCompatActivity {

    private TextView info1;
    private TextView info2;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_booking_status);

        Bundle bundle = getIntent().getExtras();


        String op = bundle.getString("content");


        info1=(TextView) findViewById(R.id.tvStatus);
        info2=(TextView) findViewById(R.id.tvPrice);

        if(op.equals("error"))
        {
            info1.setText("Booking failed.");
            info2.setText("Invalid inputs or insufficient seats.");

        }
        else
        {
            info2.setText("Price="+op);
        }





        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        getSupportActionBar().setTitle("Watch It!");

        /*FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });*/
    }

}
