package com.example.HotbarSwordMod;

import net.minecraftforge.fml.common.eventhandler.SubscribeEvent;
import net.minecraftforge.fml.common.gameevent.TickEvent;
import net.minecraftforge.common.MinecraftForge;
import net.minecraft.client.Minecraft;
import net.minecraft.item.ItemStack;
import net.minecraft.item.ItemSword;
import net.minecraft.item.Item;
import net.minecraft.init.Items;
import net.minecraft.block.Block;
import net.minecraft.init.Blocks;
import net.minecraft.entity.player.InventoryPlayer;

public class HotbarSwordMod {

    private final Minecraft mc = Minecraft.getMinecraft();

    public HotbarSwordMod() {
        // Registrierung am EventBus
        MinecraftForge.EVENT_BUS.register(this);
    }

    @SubscribeEvent
    public void onClientTick(TickEvent.ClientTickEvent event) {
        if (event.phase != TickEvent.Phase.END) return;
        if (mc.thePlayer == null) return;

        InventoryPlayer inv = mc.thePlayer.inventory;

        // Hotbar-Slot 2 → Index 1
        int targetSlot = 1;

        ItemStack current = inv.mainInventory[targetSlot];

        // Wenn schon ein Schwert da ist, nichts machen
        if (current != null && current.getItem() instanceof ItemSword) {
            return;
        }

        // Sonst: nach einem Schwert im Inventar suchen
        for (int i = 0; i < inv.mainInventory.length; i++) {
            ItemStack stack = inv.mainInventory[i];
            if (stack != null && stack.getItem() instanceof ItemSword) {
                // Tausche das Schwert in Slot 2
                inv.mainInventory[i] = current;
                inv.mainInventory[targetSlot] = stack;
                break;
            }
        }
    }

    private boolean isPickaxe(ItemStack stack) {
        if (stack == null) return false;
        Item i = stack.getItem();
        return i == Items.wooden_pickaxe || i == Items.stone_pickaxe || i == Items.iron_pickaxe
                || i == Items.golden_pickaxe || i == Items.diamond_pickaxe;
    }

    private boolean isSword(ItemStack stack) {
        if (stack == null) return false;
        Item i = stack.getItem();
        return i == Items.wooden_sword || i == Items.stone_sword || i == Items.iron_sword
                || i == Items.golden_sword || i == Items.diamond_sword;
    }

    private boolean isAxe(ItemStack stack) {
        if (stack == null) return false;
        Item i = stack.getItem();
        return i == Items.wooden_axe || i == Items.stone_axe || i == Items.iron_axe
                || i == Items.golden_axe || i == Items.diamond_axe;
    }

    private boolean isShears(ItemStack stack) {
        return stack != null && stack.getItem() == Items.shears;
    }

    private boolean isWool(ItemStack stack) {
        if (stack == null) return false;
        Block block = Block.getBlockFromItem(stack.getItem());
        return block == Blocks.wool;
    }

    private boolean isGoldenApple(ItemStack stack) {
        return stack != null && stack.getItem() == Items.golden_apple;
    }

    private boolean isFireball(ItemStack stack) {
        return stack != null && stack.getItem() == Items.fire_charge;
    }
}
