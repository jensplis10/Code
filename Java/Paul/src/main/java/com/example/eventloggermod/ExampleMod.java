package com.example.eventloggermod;

import cpw.mods.fml.common.Mod;
import cpw.mods.fml.common.event.FMLInitializationEvent;
import cpw.mods.fml.common.event.FMLPostInitializationEvent;
import cpw.mods.fml.common.event.FMLPreInitializationEvent;
import net.minecraftforge.common.MinecraftForge;

@Mod(modid = ExampleMod.MODID, name = ExampleMod.NAME, version = ExampleMod.VERSION)
public class ExampleMod {
    public static final String MODID = "eventloggermod";
    public static final String NAME = "Event Logger Mod";
    public static final String VERSION = "1.0";

    @Mod.EventHandler
    public void preInit(FMLPreInitializationEvent event) {
        System.out.println("[EventLoggerMod] FMLPreInitializationEvent");
        // Register a global event listener for Forge events
        MinecraftForge.EVENT_BUS.register(new EventLogger());
    }

    @Mod.EventHandler
    public void init(FMLInitializationEvent event) {
        System.out.println("[EventLoggerMod] FMLInitializationEvent");
    }

    @Mod.EventHandler
    public void postInit(FMLPostInitializationEvent event) {
        System.out.println("[EventLoggerMod] FMLPostInitializationEvent");
    }
}
