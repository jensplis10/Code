import com.github.kwhat.jnativehook.GlobalScreen;
import com.github.kwhat.jnativehook.NativeHookException;
import com.github.kwhat.jnativehook.keyboard.NativeKeyEvent;
import com.github.kwhat.jnativehook.keyboard.NativeKeyListener;

import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.InputEvent;

public class AutoClicker implements NativeKeyListener {

    private static volatile boolean running = false;
    private static Robot robot;

    public static void main(String[] args) {
        try {
            robot = new Robot();

            // Register global hook to intercept OS key events
            GlobalScreen.registerNativeHook();
            GlobalScreen.addNativeKeyListener(new AutoClicker());

            System.out.println("Global Hook Registered!");
            System.out.println("-> Press F6 to TOGGLE Autoclicker ON/OFF.");
            System.out.println("-> Press ESC to EXIT application.");

            // Start background worker thread for clicking
            Thread clickerThread = new Thread(() -> {
                while (true) {
                    if (running) {
                        robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
                        robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
                        robot.delay(1); // 10 clicks per second (100ms delay)
                    } else {
                        robot.delay(50); // Pause execution while inactive
                    }
                }
            });
            clickerThread.setDaemon(true);
            clickerThread.start();

        } catch (NativeHookException | AWTException e) {
            System.err.println("Failed to start application: " + e.getMessage());
        }
    }

    @Override
    public void nativeKeyPressed(NativeKeyEvent event) {
        // Toggle autoclicker state when pressing F6
        if (event.getKeyCode() == NativeKeyEvent.VC_F6) {
            running = !running;
            System.out.println("Autoclicker status: " + (running ? "RUNNING" : "STOPPED"));
        }

        // Gracefully clean up and exit on ESC key press
        if (event.getKeyCode() == NativeKeyEvent.VC_ESCAPE) {
            try {
                System.out.println("Exiting...");
                GlobalScreen.unregisterNativeHook();
                System.exit(0);
            } catch (NativeHookException e) {
                e.printStackTrace();
            }
        }
    }
}