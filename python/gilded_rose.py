# -*- coding: utf-8 -*-

from typing import List

class GildedRose(object):
    """A class representing the Gilded Rose inn's inventory management system."""

    def __init__(self, items: List['Item']):
        """Initializes the GildedRose with a list of items.

        Args:
            items (list): A list of Item objects.
        """
        self.items = items

    def _adjust_quality(self, item: 'Item', amount: int) -> None:
        """Adjusts the quality of an item, respecting the 0-50 bounds.

        Sulfuras is unaffected by this adjustment.

        Args:
            item (Item): The item whose quality is to be adjusted.
            amount (int): The amount to adjust the quality by (positive for increase, negative for decrease).
        """
        if item.name == "Sulfuras, Hand of Ragnaros":
            return

        item.quality += amount
        if item.quality > 50:
            item.quality = 50
        if item.quality < 0:
            item.quality = 0

    def _update_normal_item(self, item: 'Item') -> None:
        """Updates the quality and sell_in for normal items."""
        self._adjust_quality(item, -1)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._adjust_quality(item, -1)

    def _update_aged_brie(self, item: 'Item') -> None:
        """Updates the quality and sell_in for Aged Brie."""
        item.sell_in -= 1
        self._adjust_quality(item, 1)
        if item.sell_in < 0:
            self._adjust_quality(item, 1)

    def _update_sulfuras(self, item: 'Item') -> None:
        """Handles updates for Sulfuras, which never changes."""
        # Sulfuras never changes
        pass

    def _update_backstage_pass(self, item: 'Item') -> None:
        """Updates the quality and sell_in for Backstage passes."""
        item.sell_in -= 1
        self._adjust_quality(item, 1)
        if item.sell_in < 10:
            self._adjust_quality(item, 1)
        if item.sell_in < 5:
            self._adjust_quality(item, 1)
        if item.sell_in < 0:
            item.quality = 0

    def _update_conjured_item(self, item: 'Item') -> None:
        """Updates the quality and sell_in for Conjured items."""
        self._adjust_quality(item, -2)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._adjust_quality(item, -2)

    def update_quality(self) -> None:
        """Updates the quality and sell_in for all items in the inventory."""
        for item in self.items:
            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self._update_sulfuras(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_pass(item)
            elif item.name == "Conjured Mana Cake":
                self._update_conjured_item(item)
            else:
                self._update_normal_item(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
