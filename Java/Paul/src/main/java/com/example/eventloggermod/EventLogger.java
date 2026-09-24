package com.example.eventloggermod;

import cpw.mods.fml.common.eventhandler.SubscribeEvent;
import net.minecraftforge.event.Event;

/**
 * Very small event logger: registers on the MinecraftForge event bus and prints
 * every Event's runtime class simple name when it is fired.
 *
 * Note: This will produce a LOT of output. Use for debugging/learning only.
 */
public class EventLogger {

    @SubscribeEvent
    public void onAnyForgeEvent(Event event) {
        // Print the event class simple name
        System.out.println("[EventLogger] " + event.getClass().getSimpleName());
    }
}
