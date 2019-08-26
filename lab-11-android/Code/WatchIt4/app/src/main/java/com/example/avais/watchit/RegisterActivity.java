package com.example.avais.watchit;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class RegisterActivity extends AppCompatActivity {

    private EditText UserName;
    private EditText Pass;
    private EditText CPass;
    private TextView info;
    private Button Register;

    DatabaseHelper dh=new DatabaseHelper(this);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        UserName=(EditText)findViewById(R.id.unameText);
        Pass= (EditText)findViewById(R.id.passText);
        CPass=(EditText) findViewById(R.id.cpassText);
        Register=(Button) findViewById(R.id.regNowBtn);
        info=(TextView)findViewById(R.id.regTV);


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

    public void regButtonFunction(View v)
    {
        UserName=(EditText)findViewById(R.id.unameText);
        Pass= (EditText)findViewById(R.id.passText);
        CPass=(EditText) findViewById(R.id.cpassText);
        info=(TextView) findViewById(R.id.regTV);

        if (UserName.getText().toString().trim().equals("")  || Pass.getText().toString().trim().equals("")  || CPass.getText().toString().trim().equals(""))
        {
            info.setText("All the fields are mandatory");
            return;
        }

        if (!((Pass.getText().toString()).equals(CPass.getText().toString())))
        {
            info.setText("Password does not match.");
            return ;
        }
        else
        {
            UserDetails ud=new UserDetails();
            ud.setName(UserName.getText().toString());
            ud.setPassword(Pass.getText().toString());


            System.out.println(String.valueOf(UserName));
            System.out.println(String.valueOf(UserName));


            boolean ret=dh.insertUserDetails(ud,info);
            if(ret)
            {
                Intent intent = new Intent(RegisterActivity.this, RegisterationSuccessful.class);
                startActivity(intent);
                finish();

            }
        }

    }


   /* @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.Exit) {
            finish();
            System.exit(0);
            return true;
        }

        return super.onOptionsItemSelected(item);
    }*/

}




