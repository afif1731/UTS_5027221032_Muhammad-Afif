import { winCondition } from "../model/gamedata.model";

export const mainGame = {
    winCheck(curr_board: string[], curr_p: string) {
        for (let winArray of winCondition) {
            const [cell1, cell2, cell3] = winArray

            if(curr_board[cell1] === curr_p && curr_board[cell1] === curr_board[cell2] && curr_board[cell2] === curr_board[cell3]) {
                return curr_p;
            }
        }

        return '_';
    },
    getAllMove(index_p: number, curr_board: string[]) {
        let allMove: number[] = [];

        switch(index_p) {
            case 0:
                for(let c of [1, 3, 4]) {
                    if (curr_board[c] === '_') {
                        allMove.push(c);
                    }
                }
                break;
            case 1:
                for(let c of [0, 2, 4]) {
                    if (curr_board[c] === '_') {
                        allMove.push(c);
                    }
                }
                break;
            case 2:
                for(let c of [1, 4, 5]) {
                    if (curr_board[c] === '_') {
                        allMove.push(c);
                    }
                }
                break;
            case 3:
                for(let c of [0, 4, 6]) {
                    if (curr_board[c] === '_') {
                        allMove.push(c);
                    }
                }
                break;
            case 4:
                for(let c of [1, 2, 3, 5, 6, 7, 8]) {
                    if (curr_board[c] === '_') {
                        allMove.push(c);
                    }
                }
                break;
            case 5:
                for(let c of [2, 4, 8]) {
                    if (curr_board[c] === '_') {
                        allMove.push(c);
                    }
                }
                break;
            case 6:
                for(let c of [3, 4, 7]) {
                    if (curr_board[c] === '_') {
                        allMove.push(c);
                    }
                }
                break;
            case 7:
                for(let c of [4, 6, 8]) {
                    if (curr_board[c] === '_') {
                        allMove.push(c);
                    }
                }
                break;
            case 8:
                for(let c of [4, 5, 7]) {
                    if (curr_board[c] === '_') {
                        allMove.push(c);
                    }
                }
                break;
        }

        return allMove;
    },
    movePiece(curr_p: string, curr_board: string[], index_from: number, index_to: number) {
        if((curr_board[index_from] === curr_p) || (curr_board[index_to] === '_')) {
            curr_board[index_from] = '_';
            curr_board[index_to] = curr_p;
        }

        return curr_board
    }
}