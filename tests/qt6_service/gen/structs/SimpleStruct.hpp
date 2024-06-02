/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/03_structs.yml
 *   Object: SimpleStruct
 *   Template: qt6/struct_header.j2
 */

#pragma once
#include "Item.hpp"
#include <QObject>
#include <QDBusArgument>
#include <QDBusMessage>
#include <qqmlintegration.h>

namespace gen::structs {

/**
 * @brief An
 *   order
 */
struct SimpleStruct {
    Q_GADGET
    /**
     * @brief The item
     */
    Q_PROPERTY(Item item MEMBER item)
    /**
     * @brief the amount
     *   ordered
     */
    Q_PROPERTY(uint amount MEMBER amount)
public:
    /**
     * @brief The item
     */
    Item item;
    /**
     * @brief the amount
     *   ordered
     */
    uint amount;

    /**
     * @brief Registers MetaTypes used by this struct.
     */
    static void registerMetaTypes();
};

/**
 * @brief Marshalls a SimpleStruct into a QDBusArgument.
 *
 * @param argument the argument to marshall into
 * @param object the object to marshall
 *
 * @returns QDBusArgument the argument containing the marshalled object (same as argument)
 */
QDBusArgument &operator<<(QDBusArgument &argument, const SimpleStruct &object);

/**
 * @brief Demarshalls a SimpleStruct from a QDBusArgument.
 *
 * @param argument the argument to demarshall from
 * @param object the object to demarshall
 *
 * @returns QDBusArgument the argument containing the marshalled object (same as argument)
 */
const QDBusArgument &operator>>(const QDBusArgument &argument, SimpleStruct &object);

bool operator!=(const SimpleStruct &lhs, const SimpleStruct &rhs);

/**
 * @brief Factory to create SimpleStruct objects in QML.
 */
class SimpleStructFactory : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON
public:
    /**
     * @brief Create a SimpleStruct object.
     *
     * @param item The item
     * @param amount the amount
     *   ordered
     */
    Q_INVOKABLE SimpleStruct create (
        Item item,
        uint amount
    ) const;
};

}

Q_DECLARE_METATYPE(gen::structs::SimpleStruct)