import { Deck, Card, Suit, Rank, Color } from "./models/card"
import { Player } from "./models/player"

export const createDeck = (): Deck => {
    const deck: Deck = []
    for (const suit in Suit) {
        for (const rank in Rank) {
            const card: Card = {
                suit: Suit[suit as keyof typeof Suit],
                rank: Rank[rank as keyof typeof Rank],
                color: suit === Suit.Hearts || suit === Suit.Diamonds ? Color.Red : Color.Black,
                effect: undefined,
            }
            deck.push(card)
        }
    }
    return deck
}

export const shuffleDeck = (deck: Deck): Deck => {
    for (let i = deck.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1))
        const temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp
    }
    return deck
}


