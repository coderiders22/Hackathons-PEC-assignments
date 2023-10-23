// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
   * @title ContractName
   * @dev ContractDescription
   * @custom:dev-run-script Contract1.sol
   */

contract ArticleRegistry {
    struct Article {
        string title;
        string content;
        uint256 timestamp;
        address author;
    }

    Article[] public articles;

    mapping(uint256 => address) public articleToAuthor;

    event ArticlePosted(uint256 indexed articleId, address author);
    event ArticleUpdated(uint256 indexed articleId, address author);
    event ArticleDeleted(uint256 indexed articleId, address author);

    function postArticle(string memory _title, string memory _content) public {
        require(bytes(_title).length > 0, "Title cannot be empty");
        require(bytes(_content).length > 0, "Content cannot be empty");

        uint256 timestamp = block.timestamp; // Current block timestamp
        address author = msg.sender;

        uint256 articleId = articles.length;
        articles.push(Article({
            title: _title,
            content: _content,
            timestamp: timestamp,
            author: author
        }));

        articleToAuthor[articleId] = author;

        emit ArticlePosted(articleId, author);
    }

    function updateArticle(uint256 articleId, string memory _content) public {
        require(articleId < articles.length, "Article does not exist");
        address author = articleToAuthor[articleId];
        require(msg.sender == author, "Only the author can update the article");

        articles[articleId].content = _content;
        emit ArticleUpdated(articleId, author);
    }

    function deleteArticle(uint256 articleId) public {
        require(articleId < articles.length, "Article does not exist");
        address author = articleToAuthor[articleId];
        require(msg.sender == author, "Only the author can delete the article");

        delete articles[articleId];
        emit ArticleDeleted(articleId, author);
    }

    function getArticle(uint256 articleId) public view returns (string memory, string memory, uint256, address) {
        require(articleId < articles.length, "Article does not exist");
        Article memory article = articles[articleId];
        return (article.title, article.content, article.timestamp, article.author);
    }

    function getArticleCount() public view returns (uint256) {
        return articles.length;
    }
}