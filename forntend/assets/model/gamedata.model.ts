export interface ILocalDataSave {
    curr_p: string,
    curr_board: string[],
    move_hist: string[]
}

export enum gameStatus {
    win = 'WINNING',
    lose = 'LOSING',
    play = 'PLAYING'
}

export const winCondition = [
    //rows
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    //cols
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    //diagonal
    [0, 4, 8],
    [2, 4, 6]
]