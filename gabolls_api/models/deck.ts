// Card Game

export enum Suit {
    Hearts = "Hearts",
    Diamonds = "Diamonds",
    Clubs = "Clubs",
    Spades = "Spades",
}

export enum Color {
    Red = "Red",
    Black = "Black",
}

export enum Rank {
    Zero = "Zero",
    One = "One",
    Two = "Two",
    Three = "Three",
    Four = "Four",
    Five = "Five",
    Six = "Six",
    Seven = "Seven",
    Eight = "Eight",
    Nine = "Nine",
    Ten = "Ten",
    Jack = "Jack",
    Queen = "Queen",
    King = "King",
    Ace = "Ace",
}


export enum Effect {
    Skip = "Skip",
    Reverse = "Reverse",
    DrawTwo = "DrawTwo",
    Wild = "Wild",
    WildDrawFour = "WildDrawFour",
}


export type Card = {
    suit: Suit;
    rank: Rank;
    color: Color;
    effect?: Effect;
}

export type Deck = Card[]